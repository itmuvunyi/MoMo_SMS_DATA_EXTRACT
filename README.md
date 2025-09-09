# MoMo SMS Dashboard

## Project Overview
The MoMo SMS Dashboard is an enterprise-level fullstack application designed to process MoMo SMS data in XML format. The application will clean and categorize the data, store it in a relational database, and provide a frontend interface for analyzing and visualizing the data. This project aims to demonstrate skills in backend data processing, database management, and frontend development.

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd momo-sms-dashboard
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Copy the `.env.example` to `.env` and set the necessary environment variables, including `DATABASE_URL` or the path to the SQLite database.

5. **Run the ETL Process**
   Execute the ETL process to parse, clean, categorize, and load the data into the database:
   ```bash
   ./scripts/run_etl.sh
   ```

6. **Serve the Frontend**
   To serve the frontend dashboard, run:
   ```bash
   ./scripts/serve_frontend.sh
   ```

## Team Members
- Member 1: [Innocent Tito Muvunyi]
- Member 2: [Twariki Abdalazizi]
- Member 3: [Flavienne BENIHIRWE]

Feel free to replace the placeholder names with actual team member names.
