""""""
import json
import os
import pandas as pd

if __name__ == '__main__':
    # Get the outputs from the Grype scans
    grype_results = os.listdir("./grype-output/")

    # Sort the filenames
    grype_results.sort()

    # image names
    images = list(set([x.split('-')[0] for x in grype_results]))

    # Create a dictionary to hold results
    results = dict()

    # Load each Grype Scan
    for file in grype_results:
        with open(f'./grype-output/{file}') as f:
            # Load the json data
            data = json.load(f)

            # Append results to dictionary
            results[f"{file.replace('.json', '')}"] = len(data['matches'])

    # create a dict and DF to hold SBOM and versions data
    sboms = dict()
    versions = pd.DataFrame()

    # Load each SBOM
    for file in os.listdir("./syft-output/"):
        with open(f'./syft-output/{file}') as f:
            # Load the json data
            sbom = json.load(f)

            # Append results to dictionary
            sboms[f"{file.replace('.json', '')}"] = len(sbom['artifacts'])

            # Create a list of all the packages within the image
            temp_ver = [[file.replace('-sbom.json', ''), 
                         x['id'], 
                         x['name'], 
                         x['version'], 
                         x['type']] for x in sbom['artifacts']]
            # Create a temp DF to hold data
            temp_ver_df = pd.DataFrame(temp_ver, columns = ['image', 'id', 'name', 'version', 'type'])

            # Concat the version data back to the complete version DF
            versions = pd.concat([versions, temp_ver_df])


    # Calculate the reduction of vulnerabilities (CVEs) from the update
    for image in images:
        print(f"==============================================")
        print(f"Results for image -> {image}:latest")

        # print the number of packages in the image
        original_sbom = sboms[f"{image}-sbom"]
        print(f"    - Original package count: {original_sbom}")

        original = results[f"{image}-grype"]
        updated = results[f"{image}-updated-grype"]
        reduced_cve = original - updated

        print(f"    - Original image CVE count: {original}")
        print(f"    - Updated image CVE count: {updated}")
        print(f"    - Reduced CVE from updated image: {reduced_cve}")

        ##############################################################################################
        ##############################################################################################

        # Generate version differences from the SBOMs
        original_ver = versions[versions['image']==f"{image}"]
        updated_ver = versions[versions['image']==f"{image}-updated"]
        updated_ver = updated_ver.rename(columns={"version": "updated_version"})

        # Create a diff of the versions from merging back together
        diff_vers = original_ver[["name", "type", "version"]].merge(updated_ver[["name", 
                                                                                 "type", 
                                                                                 "updated_version"]],
                                       on=["name", "type"],
                                       how='left')
        # remove any duplicates (this can come from multiple versions of the same package in the merge)
        diff_vers = diff_vers.drop_duplicates(subset=["name", "type"])

        # check if the package version was updated
        diff_vers["update"] = diff_vers.apply(
            lambda x: True if x['version'] != x['updated_version'] else False,
            axis=1
        )

        # set updates to True
        diff_ver_updates = diff_vers[diff_vers['update']==True]

        print(f"    - Total packages updated: {len(diff_ver_updates)}")

        # print the versions that were updated
        if len(diff_ver_updates) > 0:
            for idx, row in diff_ver_updates.iterrows():
                print(f"        - {row['name']}({row['type']}): {row['version']} -> {row['updated_version']}")

        # print some useful CG stats 
        cg_cve = results[f"{image}-cg-grype"]
        print(f"\n    - Chainguard image CVE count: {cg_cve}")

        cg_sbom = sboms[f"{image}-cg-sbom"]
        print(f"    - Chainguard package count: {cg_sbom}")

        print(f"==============================================")
