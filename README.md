# 📸 Upload Image & Email Link via AWS Lambda

This project demonstrates a simple **Serverless architecture** using:

- 🧑‍💻 Static Website hosted on **Amazon S3**
- ⚙️ Backend logic using **AWS Lambda**
- 📤 Sending Emails with **Amazon SES**
- ☁️ Uploading files to **Amazon S3**

---

## 🧠 Project Flow

1. User uploads an image via the static website  
2. Image is sent to API Gateway → invokes Lambda function  
3. Lambda function:  
   - uploads image to an S3 bucket  
   - generates the image URL  
   - sends the URL via email using Amazon SES  
4. Image is accessible via public link

---

## 🖼️ Project Diagram

![Diagram](assets/diagram.svg)

---

## 🌐 Static Website

![Static Site](assets/static-site.png)

---

## 📤 Image Upload Flow

### Before Upload
![S3 Before](assets/s3-before.png)

### After Upload
![S3 After](assets/s3-after.png)

---

## ⚙️ Lambda Function

![Lambda](assets/lambda.png)

---

## 📧 Email Sent

![Email](assets/email.png)

---

## 🔗 Image Link in Email

![Image Link](assets/image-link.png)

---

## 📁 Project Structure

```bash
📁 web                # Frontend static website (HTML/JS)
📁 Lambda_Code        # Lambda function code (Python)
📁 assets             # Documentation screenshots and diagrams
