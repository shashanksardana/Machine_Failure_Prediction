from huggingface_hub import HfApi
import os

HF_TOKEN = os.getenv("HF_TOKEN")

#api = HfApi(HF_TOKEN)
api = HfApi(token=HF_TOKEN)
api.upload_folder(
    folder_path="week_2_mls/deployment",     # the local folder containing your files
    repo_id="ShashankSardana/Machine-Failure-Prediction",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
