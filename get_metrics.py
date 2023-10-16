def load_labels(file_path):
    labels = {}
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                image_name, label = parts
                labels[image_name] = label
    return labels

def calculate_metrics(labels1, labels2):
    common_images = set(labels1.keys()) & set(labels2.keys())
    true_positives = sum(1 for image in common_images if labels1[image] == 'good' and labels2[image] == 'good')
    false_positives = sum(1 for image in common_images if labels1[image] == 'ng' and labels2[image] == 'good')
    false_negatives = sum(1 for image in common_images if labels1[image] == 'good' and labels2[image] == 'ng')

    precision = true_positives / (true_positives + false_positives) if true_positives + false_positives > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if true_positives + false_negatives > 0 else 0
    f1_score = (2 * precision * recall) / (precision + recall) if precision + recall > 0 else 0

    return precision, recall, f1_score

# Load labels from two text files
labels1 = load_labels("labels.txt")
labels2 = load_labels("results.txt")

# Calculate and print precision, recall, and F1 score
precision, recall, f1_score = calculate_metrics(labels1, labels2)
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1_score:.2f}")
