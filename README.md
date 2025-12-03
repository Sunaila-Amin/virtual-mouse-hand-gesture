🖱️ Virtual Mouse Using Hand Gesture Recognition
Control your computer mouse using just your hand — no physical device needed.

This project uses Python, OpenCV, and MediaPipe to track hand movements in real time and translate them into mouse actions such as cursor movement, left click, right click, drag-and-drop, and scrolling.

🚀 Features:

🎯 Real-time cursor movement using index finger
👆 Left click using pinch gesture (thumb + index)
👉 Right click using index + middle finger
✋ Drag and Drop using pinch-hold gesture
📜 Scrolling by raising pinky
🔄 Smooth cursor movement using signal filtering
⚡ Runs at 25–30 FPS for low-latency control
🧠 Uses 21-point hand landmark detection from MediaPipe

🛠️ Tech Stack:

Python 3.10
OpenCV – Real-time video processing
MediaPipe – Hand tracking (21 landmarks)
PyAutoGUI – Simulating mouse actions
NumPy – Coordinate interpolation & smoothing

🎮 Gesture Controls
Gesture	Action
☝ Index finger up	Move cursor
👍 Pinch (index + thumb)	Left Click
✌ Index + Middle up	Right Click
🤏 Pinch hold > 0.3s	Drag & Drop
🤙 Pinky up	Scroll (Up/Down based on hand movement)

📦 Installation:
1️⃣ Clone the repository
git clone https://github.com/your-username/virtual-mouse-hand-gesture.git
cd virtual-mouse-hand-gesture

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the application
python virtual_mouse.py

📁 Folder Structure
virtual-mouse-hand-gesture/
│
├── virtual_mouse.py          # Main application
├── requirements.txt          # Required dependencies
└── README.md                 # Project documentation

🧠 How It Works

Reads webcam frames using OpenCV
MediaPipe detects 21 hand landmarks
Finger positions → Recognized using geometric rules
Gestures → Converted into mouse events
Cursor movement → Smoothed using exponential filtering
PyAutoGUI simulates real mouse actions

📈 Future Improvements:

Adding custom gesture training
Multi-hand control (left/right hand)
UI overlays for gestures
Depth estimation for more accurate detection

👤 Author

Sunaila Amin
B.Tech, Computer Science & AI
Passionate about computer vision, machine learning, and real-time applications.

LinkedIn: https://www.linkedin.com/in/sunaila-amin/
GitHub: https://github.com/Sunaila-Amin/
