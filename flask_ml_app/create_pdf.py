from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

def create_pdf():
    # Setup PDF
    c = canvas.Canvas("deployment_documentation.pdf", pagesize=letter)
    width, height = letter
    
    # Add metadata
    c.setTitle("Model Deployment Documentation")
    
    # 1. Header Section
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, height-50, "AI Model Deployment Report")
    
    c.setFont("Helvetica", 12)
    c.drawString(100, height-80, "Name: Adama")
    c.drawString(100, height-100, "Batch Code: LISUM45")
    c.drawString(100, height-120, "Submission Date: 2025-05-28")
    c.drawString(100, height-140, "Submitted to: DAta Glacier intership week 4")
    
    # 2. Add screenshots (ensure these files exist)
    screenshot_dir = "screenshots"
    screenshots = [
        ("1_model_training.png", "Step 1: Model Training Output"),
        ("2_flask_server.png", "Step 2: Flask Server Running"), 
        ("3_web_interface.png", "Step 3: Web Application"),
        ("4_prediction.png", "Step 4: Prediction Result"),
        ("5_ec2_running.png", "Step 4: Prediction Result"),
        ("6_terminal_flask.png", "Step 4: Prediction Result")


    ]
    
    y_position = height-180
    for i, (filename, description) in enumerate(screenshots):
        if os.path.exists(f"{screenshot_dir}/{filename}"):
            # Add description
            c.drawString(100, y_position, description)
            y_position -= 20
            
            # Add image (scaled to 400px width)
            img = ImageReader(f"{screenshot_dir}/{filename}")
            img_width = 400
            img_height = img._image.size[1] * (img_width/img._image.size[0])
            c.drawImage(img, 100, y_position-img_height, width=img_width, height=img_height)
            y_position -= img_height + 40
            
            # Add new page if needed
            if y_position < 100 and i < len(screenshots)-1:
                c.showPage()
                y_position = height-50
    
    # Save PDF
    c.save()
    print("PDF successfully generated!")

if __name__ == "__main__":
    create_pdf()