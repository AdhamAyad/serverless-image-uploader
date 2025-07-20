# 📸 Upload Image & Email Link via AWS Lambda

This project demonstrates a simple **Serverless architecture** using:

- 🧑‍💻 Static Website hosted on **Amazon S3**
- ⚙️ Backend logic using **AWS Lambda**
- 📤 Sending Emails with **Amazon SES**
- ☁️ Uploading files to **Amazon S3**

---

## 🖼️ Architecture Diagram

![Architecture Diagram](assets/diagram.png)

---

## 🧠 Project Flow

1. User uploads an image via the static website  
   ![Upload Form](assets/upload-form.png)

2. Image is sent to API Gateway → invokes Lambda function  
   ![Network Request](assets/request.png)

3. Lambda function:
   - uploads image to an S3 bucket
   - generates the image URL
   - sends the URL via email using Amazon SES  
   ![SES Email](assets/email.png)

4. Image is accessible via public link

---

## 📁 Project Structure

```bash
📁 web                # Frontend static website (HTML/JS)
📁 Lambda_Code        # Lambda function code (Python)
📁 assets             # Documentation screenshots and diagrams
