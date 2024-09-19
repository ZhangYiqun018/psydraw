<p align="center">
  <img src="assets/logo2.png" alt="PsychePal Logo" width="200"/>
</p>

<h1 align="center">PsychePal: AI-Assisted HTP Analysis for Left-Behind Children</h1>

<p align="center">
  <a href="https://psychepal.zeabur.app/HTP_Test">
    <img src="https://img.shields.io/badge/Demo-Live%20Website-blue?style=for-the-badge" alt="Live Demo">
  </a>
</p>

## Project Overview

PsychePal is an AI-powered tool designed to assist in the early detection of psychological issues among left-behind children through the analysis of House-Tree-Person (HTP) projective drawings. This project aims to address the widespread mental health concerns faced by children in rural areas who are separated from their parents due to economic migration.

By leveraging Large Language Models (LLMs), PsychePal provides a scalable solution to help mental health professionals and educators quickly screen and identify potential psychological issues, enabling timely intervention and support for vulnerable children.

**Important Notice:** PsychePal is intended as a screening aid only and should not replace professional psychological evaluation. All results should be interpreted and verified by qualified mental health professionals.

## Key Features

- Automated analysis of House-Tree-Person (HTP) drawings
- Multi-language support (English and Chinese)
- API for seamless integration with existing systems
- Web-based demo with built-in drawing tool and report generation

## Installation

1. Clone the repository:
```
git clone https://github.com/ZhangYiqun018/psychepal.git
cd psychepal
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Set up environment variables:
- Copy the `.env_example` file and rename it to `.env`
- Fill in your API key and base URL in the `.env` file

## Usage

### 1. Direct Invocation

```bash
bash run.sh
```
or
```bash
python run.py \
    --image_file example/example1.png \
    --save_path example/example1_result.json \
    --language en 
```

### 2. API Integration

Start the API server:
```bash
python deploy.py --port 9557
```

The service will run on `http://127.0.0.1:9557`. It accepts HTTP requests with `image_path` and `language` parameters.

### 3. Web Demo

Launch the web demonstration:
```bash
bash web_demo.sh
```
or
```bash
streamlit run src/main.py
```

The web demo includes a built-in drawing board, supports image upload, and provides report generation and download functionality.


## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

PsychePal is a research and screening aid tool only. It should not be used as a diagnostic tool or a substitute for professional medical advice. Users assume full responsibility for any decisions or actions based on the use of this tool.

## Ethical Considerations

The psychological well-being of children is a sensitive and critical matter. PsychePal is designed to support, not replace, the crucial role of mental health professionals and caregivers. Users must ensure that the tool is used ethically, maintaining the privacy and best interests of the children at all times.