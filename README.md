# ansible-aws-headlesschrome

AnsibleでAWS上にOpenSUSEでGoogle Chromeをヘッドレス実行可能な環境を構築するPlaybookです。

## Overview

- SeleniumのwebdriverでGoogle Chromeをヘッドレス実行してスクリーンショットを撮りたい
- AWS EC2のOpenSUSE上で Python + Selenium + chromedriver を利用
- この環境をEC2インスタンスの作成からAnsibleで構築

![overview](https://qiita-image-store.s3.amazonaws.com/0/199081/e62f0d1a-fd35-a7a1-91da-317b67ca2c26.png)

## Requirements
- ansible 2.4 or later
- boto

## Usage

### Download
適当なディレクトリにPlaybookをダウンロードしてください。

```
$ git clone https://github.com/rednes/ansible-aws-headlesschrome.git
$ cd ansible-aws-headlesschrome
```

### Edit ansible.cfg

ansible.cfg.sampleファイルがあるので、ansible.cfgにコピーしてください。
```
$ cp ansible.cfg.sample ansible.cfg
```

ansible.cfgのprivate_key_fileに、AWSに登録している秘密鍵のパスを記載してください。

```
[defaults]
inventory = hosts/ec2.py
retry_files_enabled = False
private_key_file=XXXXXX.pem # set your environment

[privilege_escalation]
become = False

[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null
```

### Edit all.yml

group_varsフォルダにall.yml.sampleファイルがあるので、all.ymlにコピーしてください。
```
$ cp group_vars/all.yml.sample group_vars/all.yml
```

key_nameに、AWSに登録しているキーペア名を記載してください。

```
---
my_vars:
  ec2:
    key_name: XXXX # AWSに登録したキーペア名を入力
```

### Execute ansible

ansibleを実行するとAWS環境と作成したEC2にChromeをヘッドレス実行可能な環境を構築します。

```
$ ansible-playbook site.yml -v
```

### Check

SSHで作成したEC2に接続し、ホームフォルダにあるsample.pyを実行してください。

```
$ python sample.py
```

数秒で実行が完了し、同フォルダにscreenshot.pngが作成されます。
こんな風にスクリーンショットが撮れていれば動作できていると思います。

![check](https://qiita-image-store.s3.amazonaws.com/0/199081/0431d4d8-4928-19b4-c31d-cd1678688877.png)
