# Mathematical Reasoning in Large Language Models: Assessing Logical and Arithmetic Errors across Wide Numerical Ranges

## Dataset Information

The sample dataset for GSM-Ranges can be found in the `sample_dataset` folder. It includes **50 different sets of 100 questions** for each perturbation level. This dataset provides a structured way to analyze the impact of numerical range perturbations on the reasoning abilities of large language models.

## Generating Your Own Dataset

If you wish to generate your own dataset, you can use the provided Python script. Run the following command:

```sh
python generate_dataset.py --output_dir YOUR_OUTPUT_DIRECTORY --set_num NUMBER_OF_SETS
```

where:
- `--output_dir` specifies the directory where the generated dataset should be saved.
- `--set_num` determines the number of sets to generate.

---
