import json

# Define a list of copyleft licenses to flag
COPYLEFT_LICENSES = ["GPL", "AGPL", "LGPL", "Affero", "MPL", "EPL", "CC-BY-SA"]

# Load the ScanCode output
with open('output.json', 'r') as f:
    scan_data = json.load(f)

flagged_licenses = []

# Check for copyleft licenses in the detected licenses
for license_detection in scan_data.get('license_detections', []):
    for copyleft in COPYLEFT_LICENSES:
        if copyleft in license_detection['license_expression_spdx']:
            flagged_licenses.append(license_detection)

# Flag if any copyleft licenses are found
if flagged_licenses:
    print("Copyleft licenses detected! The following licenses were flagged:")
    for license in flagged_licenses:
        print(f"- {license['license_expression_spdx']} found in file {license['reference_matches'][0]['from_file']}")
    exit(1)  # Exit with error code to fail the pipeline
else:
    print("No copyleft licenses found.")
