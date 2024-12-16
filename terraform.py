import subprocess

def terraform_run(command):
    process = subprocess.run(command, shell=True,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(process.stdout.decode())
directory = "D:\Python\Terraform-automation"
command = f"terraform -chdir={directory} init"
terraform_run(command)