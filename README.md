# 🚀 AI Resume Analyzer 3D

**Professional AI-powered resume analysis with stunning 3D visualization**

An advanced resume analyzer application that uses artificial intelligence to evaluate your resume, identify skill gaps, calculate ATS scores, and provide personalized career recommendations through an immersive 3D neural core interface.

---

## ✨ Features

### 🎯 **Core Analysis**
- **ATS Score Calculation** (0-100%): Determine how well your resume matches specific job roles
- **Skill Detection**: Automatically identify technical and soft skills from your resume
- **Career Matching**: Get ranked recommendations for the top 5 job positions
- **Missing Skills Analysis**: Identify critical gaps and priority areas for development

### 🎨 **3D Interactive Interface**
- **Neural Core Visualization**: Rotating 3D icosahedron with animated orbiting particles using Three.js
- **Starfield Background**: 120 animated stars for immersive dark mode experience
- **Drag & Drop Upload**: Simply drag your resume PDF into the upload zone
- **Real-time Processing**: Instant analysis with scanner animation feedback
- **Smooth Animations**: Professional transitions and hover effects throughout

### 📊 **Comprehensive Reporting**
- **Best Role Match**: Detailed compatibility analysis with percentage scores
- **Skills Breakdown**: Visual separation of found vs. missing skills with color coding
- **Learning Roadmap**: Week-by-week skill development plan with priority levels
- **Career Rankings**: Top 5 job matches with individual match percentages
- **Personalized Recommendations**: Actionable advice based on your profile

### 🎮 **Interactive Controls**
- **Mouse Drag**: Rotate the 3D neural core to explore from different angles
- **Touch Support**: Full touch gesture support for mobile devices
- **Responsive Design**: Adapts beautifully to all screen sizes
- **Professional UI**: Dark mode with gradient accents and glassmorphism effects

---

## 🏗️ **Project Structure**

```
resume-builder/
├── run_server.py                      # Main HTTP server (start here!)
├── ai_resume_analyzer_3d_dark.html    # 3D interface & core logic
├── skills.py                          # Job roles & skills database
├── app.py                             # Alternative Streamlit interface
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
├── .venv/                             # Virtual environment
├── functionalsample.pdf               # Sample resume for testing
└── resume-sample.pdf                  # Additional test resume
```

---

## 🚀 **Quick Start**

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- A modern web browser (Chrome, Firefox, Edge, Safari)

### Installation

1. **Clone/Download the project**
   ```bash
   cd "resume builder"
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   - **Windows (PowerShell):**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD):**
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **Mac/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Start the server**
   ```bash
   python run_server.py
   ```

6. **Open in browser**
   - Automatic: Browser opens automatically at `http://localhost:8000`
   - Manual: Navigate to `http://localhost:8000` or `http://127.0.0.1:8000`

---

## 📖 **How to Use**

### 1. **Access the Application**
   - Run the server and the 3D analyzer loads in your browser
   - Interact with the rotating neural core using your mouse

### 2. **Upload Your Resume**
   - **Method 1**: Click the upload zone and select a PDF file
   - **Method 2**: Drag and drop a PDF file directly into the upload zone
   - Supported format: PDF files only

### 3. **Wait for Analysis**
   - Watch the scanner animation as your resume is processed
   - Processing takes 1-2 seconds

### 4. **Review Results**
   - **Best Match**: Your top recommended job role
   - **ATS Score**: How well your resume matches the best role (0-100%)
   - **Career Grid**: Top 5 job positions ranked by compatibility
   - **Skills Panel**: 
     - ✅ Green tags = Skills found in your resume
     - ❌ Red tags = Missing skills for the best role
   - **Learning Roadmap**: Week-by-week skill development plan
   - **Rating Card**: Visual assessment (Excellent/Good/Needs Improvement)

### 5. **Take Action**
   - Follow the personalized recommendations
   - Use the learning roadmap to plan your development
   - Focus on high-priority missing skills first

---

## 🛠️ **Technology Stack**

| Component | Technology | Version |
|-----------|-----------|---------|
| **Frontend** | HTML5 + JavaScript | Modern ES6+ |
| **3D Graphics** | Three.js | r128 |
| **Server** | Python HTTP Server | Built-in |
| **Backend Logic** | Python 3 | 3.7+ |
| **UI Framework** | CSS3 (Glassmorphism) | Modern |
| **Data Analysis** | Custom JS Algorithm | - |

---

## 📊 **Supported Job Roles**

The analyzer can evaluate your resume against these positions:

1. **Data Scientist**
   - Python, Machine Learning, Deep Learning, SQL, Pandas

2. **Frontend Developer**
   - JavaScript, React, HTML/CSS, TypeScript, Vue.js

3. **Backend Developer**
   - Python, Node.js, Django, PostgreSQL, REST API

4. **DevOps Engineer**
   - Docker, Kubernetes, AWS, CI/CD, Linux

5. **Cybersecurity Analyst**
   - Network Security, Penetration Testing, SIEM, Firewalls

6. **ML Engineer**
   - TensorFlow, PyTorch, Python, MLOps, Data Engineering

---

## 🎯 **How Analysis Works**

### ATS Score Calculation
The system analyzes your resume PDF to:
1. Extract text content
2. Match against job-specific skill requirements
3. Calculate compatibility percentage
4. Rank alternative career paths

### Skill Matching Algorithm
- **Found Skills**: Keywords from your resume that match job requirements
- **Missing Skills**: Required skills not detected in your resume
- **Priority Calculation**: Based on criticality for the target role

### Learning Roadmap Generation
- Prioritizes high-impact skills first
- Estimates learning time (2-4 weeks per skill)
- Groups related skills together
- Provides structured progression path

---

## 🎨 **Design Features**

### Visual Design
- **Dark Mode**: Reduces eye strain with professional dark theme
- **Gradient Accents**: Purple to blue gradient scheme
- **Glassmorphism**: Modern frosted glass effect on cards
- **Animations**: Smooth transitions and micro-interactions
- **Responsive Grid**: Adapts from mobile to desktop

### Accessibility
- High contrast colors for readability
- Clear visual hierarchy
- Intuitive navigation
- Keyboard friendly
- Touch gesture support

---

## ⚙️ **Configuration**

### Server Port
- **Default**: `http://localhost:8000`
- **To change**: Edit `run_server.py` and change `PORT = 8000`

### Job Roles Database
- **Location**: `skills.py`
- **To add roles**: Add new entries to the `jobRoles` dictionary
- **Format**: `"Role Name": ["skill1", "skill2", ...]`

---

## 🐛 **Troubleshooting**

### Server Won't Start
**Problem**: Port already in use
```bash
# Solution 1: Wait 30-60 seconds and try again
# Solution 2: Change PORT in run_server.py to 8001, 8002, etc.
# Solution 3: Find and close other apps using the port
```

### Resume Not Uploading
**Problem**: File format or size issues
```
- Ensure file is PDF format
- File size should be under 10 MB
- Try a different PDF reader to create your resume
```

### 3D Visualization Not Appearing
**Problem**: Browser compatibility or JavaScript
```
- Use a modern browser (Chrome 90+, Firefox 88+, Edge 90+, Safari 14+)
- Clear browser cache and refresh
- Try a different browser
```

### Analysis Shows No Skills
**Problem**: Resume format not recognized
```
- Ensure skills are written as keywords (e.g., "Python", "React")
- Avoid images in resume - text must be selectable
- Convert image-based PDF to text-based PDF
```

---

## 📝 **Sample Resumes**

The project includes two sample resumes for testing:
- `functionalsample.pdf` - Functional resume format
- `resume-sample.pdf` - Chronological resume format

Try uploading these to see the analyzer in action!

---

## 🔐 **Privacy & Security**

- **Local Processing**: All analysis happens in your browser
- **No Cloud Storage**: Your resume is never uploaded to external servers
- **No Data Collection**: We don't track or store your resume data
- **Instant Analysis**: Results generated in real-time on your machine

---

## 📈 **Performance**

- **Analysis Speed**: < 2 seconds
- **Initial Load**: < 1 second
- **3D Rendering**: 60 FPS on modern devices
- **Browser Support**: All modern browsers
- **Mobile Support**: Fully responsive design

---

## 🎓 **Learning Resources**

To improve your resume based on recommendations:

1. **Skill Development**
   - Online courses: Coursera, Udemy, LinkedIn Learning
   - Certifications: AWS, Google Cloud, Azure
   - Practice platforms: LeetCode, HackerRank, Kaggle

2. **Resume Writing**
   - Use strong action verbs
   - Quantify achievements with metrics
   - Keep it concise (1-2 pages)
   - Tailor to each job posting

3. **Career Planning**
   - Follow the learning roadmap
   - Build portfolio projects
   - Contribute to open source
   - Network with professionals

---

## 🤝 **Contributing**

Improvements and suggestions welcome! Areas for enhancement:
- Additional job role categories
- Multi-language support
- Advanced skill extraction
- Export functionality
- Extended skill database

---

## 📄 **License**

This project is provided as-is for educational and professional use.

---

## 📧 **Support**

For issues or questions:
1. Check the Troubleshooting section above
2. Verify all dependencies are installed
3. Ensure Python 3.7+ is being used
4. Try the sample resumes first

---

## 🚀 **Future Roadmap**

- [ ] PDF text extraction improvements
- [ ] Industry-specific analysis modes
- [ ] Salary predictions
- [ ] Network analysis
- [ ] Job market insights
- [ ] Resume templates
- [ ] Interview preparation

---

## ⭐ **Key Highlights**

✅ **Zero Setup Required** - Works out of the box  
✅ **Beautiful UI** - Professional 3D visualization  
✅ **Fast Processing** - Real-time analysis  
✅ **Privacy First** - All local, no cloud required  
✅ **Easy to Use** - Intuitive drag & drop interface  
✅ **Comprehensive** - Full skill and career analysis  

---

## 🎯 **Get Started Now!**

```bash
python run_server.py
```

Then open your browser to `http://localhost:8000` and upload your resume! 🚀

---

**Version**: 1.0  
**Last Updated**: June 2026  
**Status**: ✅ Production Ready
