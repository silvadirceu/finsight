from huggingface_hub import hf_hub_download
hf_hub_download(repo_id="TheBloke/firefly-llama2-7B-chat-GGUF", filename="firefly-llama2-7b-chat.Q5_K_M.gguf", local_dir="./llama2_api/.cache",
local_dir_use_symlinks=False)
