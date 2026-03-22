♻️ Smart Biomedical Waste Segregation using AI
📌 Overview

This project is an AI-powered smart waste segregation system that uses computer vision to detect and classify biomedical waste in real-time using a webcam. The system intelligently categorizes waste into different types and simulates bin management, making it a step toward automated waste handling systems.

🚀 Features
🎥 Real-time waste detection using webcam
🧠 AI-based image classification using deep learning
🏥 Biomedical waste classification (12 classes → 4 categories)
📊 Smart bin level monitoring (simulated on laptop)
🔌 Ready for Arduino & Raspberry Pi integration
⚡ Fast and efficient detection system
🧠 Waste Categories
🔴 Hazardous Waste
Body Tissue / Organs
Syringe Needles
Syringes
🟢 Plastic Waste
Plastic Equipment
Gloves
Masks
🔵 Metal / Glass Waste
Metal Equipment
Glass Equipment
Tweezers
🟡 General Waste
Organic Waste
Paper
Gauze
🛠️ Tech Stack
Python 🐍
TensorFlow / Keras 🤖
OpenCV 📷
NumPy 📊
Arduino (future hardware integration)
Raspberry Pi (planned deployment)
⚙️ How It Works
📷 Webcam captures live video
🧠 AI model processes image frame
🔍 Waste is classified into category
📊 System updates bin status
⚙️ (Future) Signal sent to Arduino for sorting
▶️ How to Run
# Install dependencies
pip install tensorflow opencv-python numpy

# Run the system
python smart_system.py
📁 Project Structure
bio_project/
│── train.py
│── smart_system.py
│── live_webcam.py
│── README.md
│── .gitignore
🔮 Future Scope
🔌 Arduino-based automatic sorting system
🤖 Raspberry Pi deployment
📱 Mobile app integration
📊 IoT dashboard for monitoring bin levels
🎯 Improved model accuracy with larger dataset
🎯 Applications
Hospitals & healthcare waste management
Smart cities
Automated recycling systems
Environmental sustainability
👨‍💻 Author

Nikhil Jadhav
B.Tech CSE (Data Science)

🌟 Acknowledgment

This project is part of my learning journey in AI, IoT, and real-time system development.
