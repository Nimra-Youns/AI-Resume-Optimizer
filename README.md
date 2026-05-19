# AI Resume & Cover Letter Optimizer

An intelligent application that uses Claude AI to analyze your resume and cover letter, tailor them to specific job applications, research market trends, and provide AI-powered rewriting suggestions.

## 🚀 Features

- **Resume Analysis** - Parse and analyze your resume with Claude AI
- **Cover Letter Tailoring** - Generate customized cover letters for specific job postings
- **Market Trend Research** - Analyze current job market demands and skills trends
- **AI Rewriting** - Get intelligent suggestions to improve language, impact, and relevance
- **Multi-Document Support** - Process multiple resumes and cover letters
- **Export Ready** - Generate formatted output ready for applications

## 📋 Tech Stack

- **Python 3.10+**
- **Claude API (via Anthropic SDK)**
- **PDF Processing (pypdf)**
- **File I/O & Document Handling**

## 🛠️ Installation

### Prerequisites
- Python 3.10 or higher
- API key from [Anthropic](https://console.anthropic.com)

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/NIMRA-YOUNS/ai-resume-optimizer/issues
cd ai-resume-optimizer
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API key**
```bash
cp config.example.py config.py
# Edit config.py and add your Anthropic API key
```

## 📖 Usage

### Basic Example

```python
from app import ResumeOptimizer

# Initialize the optimizer
optimizer = ResumeOptimizer(api_key="your-api-key")

# Load your documents
resume = optimizer.load_resume("path/to/resume.txt")
job_description = optimizer.load_job_description("path/to/job_posting.txt")

# Get AI-powered suggestions
suggestions = optimizer.get_tailored_cover_letter(resume, job_description)
market_analysis = optimizer.analyze_market_trends(job_description)
rewritten = optimizer.rewrite_resume_section(resume, "professional_summary")

# Export results
optimizer.export_to_file(suggestions, "tailored_cover_letter.txt")
```

### Command Line Usage

```bash
python app.py --resume resume.txt --job job_description.txt --output results.txt
```

## 📂 Project Structure

```
ai-resume-optimizer/
├── README.md
├── app.py                 # Main application code
├── config.example.py      # Example configuration
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
├── LICENSE               # MIT License
├── samples/
│   ├── sample_resume.txt
│   ├── sample_job_description.txt
│   └── sample_output.txt
└── docs/
    └── API_REFERENCE.md
```

## 🔑 API Features Used

### Claude AI Capabilities

1. **Document Understanding** - Extract and analyze document structure
2. **Content Generation** - Create customized cover letters and suggestions
3. **Market Analysis** - Identify trending skills and requirements
4. **Language Enhancement** - Improve clarity, impact, and professionalism
5. **Contextual Rewriting** - Adapt content for specific audiences

### API Models

This project uses the latest Claude models from Anthropic:
- `claude-opus-4-6` - For complex analysis and generation
- `claude-sonnet-4-6` - For efficient, cost-effective processing

## 📊 Use Cases

✅ Job seekers tailoring applications  
✅ Career changers repositioning experience  
✅ Freelancers customizing proposals  
✅ Recruiters analyzing candidate fit  
✅ Career coaches coaching clients  

## 🎯 Key Capabilities

### 1. Resume Analysis
Analyzes your resume for:
- Keyword relevance
- Skill alignment with job postings
- Experience positioning
- Format and readability

### 2. Cover Letter Generation
Creates customized cover letters that:
- Address specific job requirements
- Highlight relevant experience
- Match company culture
- Include compelling narratives

### 3. Market Trend Research
Provides insights on:
- In-demand skills for your role
- Salary trends and benchmarks
- Industry growth areas
- Emerging technologies

### 4. Smart Rewriting
Offers suggestions for:
- Action verb optimization
- Impact statement enhancement
- Clarity improvements
- ATS (Applicant Tracking System) optimization

## 🔐 Security & Privacy

- Your API key is stored locally and never shared
- Documents are processed via secure Anthropic API
- No data is stored on external servers
- Complies with data privacy standards

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Anthropic API Configuration
API_KEY = "your-anthropic-api-key"
MODEL = "claude-opus-4-6"
MAX_TOKENS = 2000
TEMPERATURE = 0.7

# Processing Options
EXTRACT_KEYWORDS = True
ANALYZE_SKILLS = True
GENERATE_COVER_LETTER = True
RESEARCH_MARKET_TRENDS = True
```

## 🚀 Getting Your API Key

1. Visit [Anthropic Console](https://console.anthropic.com)
2. Create an account or sign in
3. Navigate to API Keys section
4. Generate a new API key
5. Copy and paste it into `config.py`

## 📈 Results & Examples

### Input
```
Resume: 5 years in project management
Job Description: Seeking Project Manager with Agile experience
```

### Output
```
✓ Tailored Cover Letter
✓ Keyword Recommendations
✓ Market Trend Analysis
✓ Rewritten Professional Summary
✓ ATS Optimization Suggestions
```

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/ai-resume-optimizer/issues)
- **Documentation**: See `/docs` folder
- **API Help**: [Anthropic Documentation](https://docs.claude.com)

## 🌟 Roadmap

- [ ] PDF resume parsing
- [ ] LinkedIn profile integration
- [ ] Real-time job board scraping
- [ ] Resume ATS scoring
- [ ] Interactive web dashboard
- [ ] Batch processing for multiple jobs
- [ ] Email automation features

## 💡 Tips for Best Results

1. **Provide clear context** - Include complete job descriptions
2. **Update regularly** - Keep your resume current with achievements
3. **Be specific** - More details lead to better suggestions
4. **Review output** - Always review AI suggestions before using
5. **Iterate** - Use feedback to refine future applications

## 📞 Contact

- **Author**: Nimra Youns
- **Email**: nimrayous@gmail.com
- **LinkedIn**: [linkedin.com/in/nimra-youns](linkedin.com/in/nimra-youns-53a679238)
- **GitHub**: [@nimra-youns](https://github.com/nimra-youns)

---

**Built with Claude AI by Anthropic** 🤖

Made with ❤️ for job seekers and career builders
