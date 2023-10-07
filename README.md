# python-gpt

## Getting Started
Clone Repository
```
git clone https://github.com/engageintellect/python-gpt.git
```

### Setup Environment

Create a config file for your OpenAI API key
```
sudo nvim /etc/python-gpt.json
```
It should look something like this:
```
{
		"OPENAI_API_KEY": "<your key here>"
}
```
```
cd python-gpt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run
```
uvircorn main:app --reload
```








