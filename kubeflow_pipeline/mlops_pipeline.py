import kfp
from kfp import dsl
from kfp.dsl import Input, Output, Dataset, Model, component

# ✅ Data Processing Component
@component(
    base_image="vedaantkadu/my-mlops-app:latest"
)
def data_processing():
    import subprocess
    subprocess.run(["python", "src/data_processing.py"])

# ✅ Model Training Component
@component(
    base_image="vedaantkadu/my-mlops-app:latest"
)
def model_training():
    import subprocess
    subprocess.run(["python", "src/model_training.py"])

# ✅ Pipeline
@dsl.pipeline(
    name="MLOPS PIPELINE",
    description="This is my first kubeflow pipeline"
)
def mlops_pipeline():
    dp_task = data_processing()
    mt_task = model_training()
    mt_task.after(dp_task)

# ✅ Compile
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline_func=mlops_pipeline,
        package_path="mlops_pipeline.yaml"
    )
