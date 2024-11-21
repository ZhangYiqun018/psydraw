<p align="center">
  <img src="assets/logo2.png" alt="PsyDraw Logo" width="200"/>
</p>

<h1 align="center">PsyDraw: A Multi-Agent Multimodal System for Mental Health Detection in Left-Behind Children</h1>

<p align="center">
  <a href="https://psysraw.zeabur.app/HTP_Test">
    <img src="https://img.shields.io/badge/Demo-Live%20Website-blue?style=for-the-badge" alt="Live Demo">
  </a>
</p>

## Project Overview
Left-behind children (LBC) face severe mental health challenges due to parental migration for work. The House-Tree-Person (HTP) test, a psychological assessment method with higher child participation and cooperation, requires expert interpretation, limiting its application in resource-scarce areas. To address this, we propose **PsyDraw**, a multi-agent system based on Multimodal Large Language Models for automated analysis of HTP drawings and assessment of LBC's mental health status. The system's workflow comprises two main stages: feature analysis and report generation, accomplished by multiple collaborative agents. We evaluate the system on HTP drawings from 290 primary school students, with the generated mental health reports evaluated by class teachers. Results show that 71.03\% of the analyses are rated as **Matching**, 26.21\% as **Generally Matching**, and only 2.41\% as **Not Matching**. These findings demonstrate the potential of PsyDraw in automating HTP test analysis, offering an innovative solution to the shortage of professional personnel in mental health assessment for LBC.

**Important Notice:** PsyDraw is intended as a screening aid only and should not replace professional psychological evaluation. All results should be interpreted and verified by qualified mental health professionals.

<p align="center">
  <img src="assets/workflow.png" alt="PsyDraw Workflow"/>
  Figure1: The workflow of PsyDraw.
</p>

## Key Features

- Automated analysis of House-Tree-Person (HTP) drawings
- Multi-language support (English and Chinese)
- API for seamless integration with existing systems
- Web-based demo with built-in drawing tool and report generation

## Installation

1. Clone the repository:
```
git clone https://github.com/ZhangYiqun018/psysraw.git
cd PsyDraw
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

The web demo inc

### 4. Packaging the Application
Use PyInstaller to package the application:
```bash
pyinstaller htp_analyzer.spec
```
This will generate an executable file located in the `dist/htp_analyzer` directory. You can run the executable to start the HTP Analyzer.
## Case Study
<p float="left">
  <img src="assets/case_study1.png" width="45%" />
  <img src="assets/case_study2.png" width="45%" /> 
</p>

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

PsyDraw is a research and screening aid tool only. It should not be used as a diagnostic tool or a substitute for professional medical advice. Users assume full responsibility for any decisions or actions based on the use of this tool.

## Ethical Considerations

The psychological well-being of children is a sensitive and critical matter. PsyDraw is designed to support, not replace, the crucial role of mental health professionals and caregivers. Users must ensure that the tool is used ethically, maintaining the privacy and best interests of the children at all times.