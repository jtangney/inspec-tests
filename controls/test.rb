# gcp_project_id = input('gcp_project_id')
# bucket = input('bucket_name')
# input('bucket_name')
bucket_prefix = input('bucket_name_prefix', value: '')
# input('bucket_name_prefix', '')

control "validate bucket" do
  title "validating bucket"
  desc "Exciting compliance checks for GCS bucket"
  impact 0.5

  describe google_storage_bucket(name: input('bucket_name')) do
    its('storage_class') { should eq "STANDARD" }
    its('name') { should match(/^#{bucket_prefix}/) }
  end
end