import os
import re
import pandas as pd
import importlib.util
import argparse

def process_templates(output_dir_path, set_num):
    templates_dir_path = './templates'
    
    original = []
    level1 = []
    level2 = []
    level3 = []
    level4 = []
    level5 = []
    level6 = []

    for filename in os.listdir(templates_dir_path):
        match = re.match(r'(\d+)\.py$', filename)
        if match:
            file_path = os.path.join(templates_dir_path, filename)
            index = int(match.group(1))
            module_name = "q" + match.group(1)

            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            func = getattr(module, module_name)

            qa_original = func(num_level=1, name_level=1, is_symbolic=False)
            original.append({"index": index, "question": qa_original["question"], "answer": qa_original["answer"]})

            for _ in range(set_num):
                qa_level1 = func(num_level=2, multiplier=100, name_level=1, is_symbolic=False)
                level1.append({"index": index, "question": qa_level1["question"], "answer": qa_level1["answer"]})
                qa_level2 = func(num_level=4, multiplier=100, name_level=1, is_symbolic=False)
                level2.append({"index": index, "question": qa_level2["question"], "answer": qa_level2["answer"]})
                qa_level3 = func(num_level=4, multiplier=1000, name_level=1, is_symbolic=False)
                level3.append({"index": index, "question": qa_level3["question"], "answer": qa_level3["answer"]})
                qa_level4 = func(num_level=4, multiplier=10000, name_level=1, is_symbolic=False)
                level4.append({"index": index, "question": qa_level4["question"], "answer": qa_level4["answer"]})
                qa_level5 = func(num_level=4, multiplier=100000, name_level=1, is_symbolic=False)
                level5.append({"index": index, "question": qa_level5["question"], "answer": qa_level5["answer"]})
                qa_level6 = func(num_level=4, multiplier=1000000, name_level=1, is_symbolic=False)
                level6.append({"index": index, "question": qa_level6["question"], "answer": qa_level6["answer"]})

    os.makedirs(output_dir_path, exist_ok=True)
    
    pd.DataFrame(original).sort_values(by="index").reset_index(drop=True).to_csv(f"{output_dir_path}/original.csv", index=False)
    pd.DataFrame(level1).sort_values(by="index").reset_index(drop=True).to_csv(f"{output_dir_path}/level1.csv", index=False)
    pd.DataFrame(level2).sort_values(by="index").reset_index(drop=True).to_csv(f"{output_dir_path}/level2.csv", index=False)
    pd.DataFrame(level3).sort_values(by="index").reset_index(drop=True).to_csv(f"{output_dir_path}/level3.csv", index=False)
    pd.DataFrame(level4).sort_values(by="index").reset_index(drop=True).to_csv(f"{output_dir_path}/level4.csv", index=False)
    pd.DataFrame(level5).sort_values(by="index").reset_index(drop=True).to_csv(f"{output_dir_path}/level5.csv", index=False)
    pd.DataFrame(level6).sort_values(by="index").reset_index(drop=True).to_csv(f"{output_dir_path}/level6.csv", index=False)
    
    print("Processing completed. CSV files saved to:", output_dir_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Python templates and generate CSVs.")
    parser.add_argument("output_dir", type=str, help="Directory for output CSV files")
    parser.add_argument("set_num", type=int, help="Number of sets to generate")
    
    args = parser.parse_args()
    process_templates(args.output_dir, args.set_num)