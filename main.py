import os


def count_mappings(directory, mappingAnnotation):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    # count += content.count("@GetMapping")
                    count += content.count(mappingAnnotation)
    return count


project_directory = "/Users/kidd.curious/IDE/eva-channel-admin/src/main/java"
mappingAnnotations = ["@GetMapping", "@PostMapping", "@PutMapping", "@DeleteMapping"]
annotation_counts = {}

# get_mapping_count = count_get_mappings(project_directory, "@GetMapping")
for annotation in mappingAnnotations:
    annotation_counts[annotation] = count_mappings(project_directory, annotation)

# Print the annotation_counts dictionary
# print("Annotation counts dictionary:", annotation_counts.items())

for annotation, count in annotation_counts.items():
    print(f"Number of {annotation} annotations: {count}")
