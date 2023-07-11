""""""
import json
import os

if __name__ == '__main__':
    # Get the outputs from the Grype scans
    grype_results = os.listdir("./grype-output/")

    # Sort the filenames
    grype_results.sort()

    # image names
    images = list(set([x.split('-')[0] for x in grype_results]))

    # Create a dictionary to hold results
    results = dict()

    # Load each scan
    for file in grype_results:
        with open(f'./grype-output/{file}') as f:
            # Load the json data
            data = json.load(f)

            # Append results to dictionary
            results[f"{file.replace('.json', '')}"] = len(data['matches'])

    # Calculate the reduction of vulnerabilities from the update
    for image in images:
        print(f"==============================================")
        print(f"Results for image -> {image}:latest")

        original = results[f"{image}-grype"]
        updated = results[f"{image}-updated-grype"]
        reduced_vulns = original - updated

        print(f"    - Original image vuln count: {original}")
        print(f"    - Updated image vuln count: {updated}")
        print(f"    - Reduced vulns from updated image: {reduced_vulns}")

        cg_vulns = results[f"{image}-cg-grype"]
        print(f"    - Chainguard image vuln count: {cg_vulns}")

        print(f"==============================================")
