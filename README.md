# Kafka-Python-Demo

A simple Python demo showcasing the use of **Kafka** with **KRaft mode** using **Poetry** for dependency management. This project contains a producer that sends real-time temperature data and a consumer that listens for messages.

---

## 🚀 Features
- **Real-time data streaming** with Kafka
- **Command-line interface** to specify topic and consumer group
- **Dockerized Kafka setup** using the latest version (KRaft mode, no ZooKeeper needed)
- **Poetry** for managing Python dependencies

---

## 📝 Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed and running.
- [Poetry](https://python-poetry.org/docs/#installation) installed.
- Python 3.8+ installed.

---

## 🐋 Kafka Setup (Docker)
1. **Pull the Kafka Docker image:**
   ```bash
   docker pull apache/kafka:3.9.0
   ```
2. **Run the Kafka container:**
   ```bash
   docker run -p 9092:9092 apache/kafka:3.9.0
   ```
---

## 🧰 Project Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Kafka-python-Demo.git
   cd Kafka-python-Demo
   ```

2. **Install dependencies with Poetry:**
   ```bash
   poetry install
   ```

3. **Activate the Poetry shell:**
   ```bash
   poetry shell
   ```

---

## 📦 Producer Usage
The producer sends real-time temperature data to a Kafka topic.

```bash
python producer.py -t <topic-name>
```

🔔 **Example:**
```bash
python producer.py -t temp-topic
```
You will be prompted to enter the location and temperature repeatedly.

---

## 📥 Consumer Usage
The consumer listens to messages from a Kafka topic.

```bash
python consumer.py -t <topic-name> -u <consumer-group>
```

🔔 **Example:**
```bash
python consumer.py -t temp-topic -u temperature-consumer-group
```

💡 **Output:**
```
Start consuming on topic: temp-topic, usergroup: temperature-consumer-group
New Message: {'loc': 'New York', 'value': '25'}
```

---

## 🗂️ Project Structure
```
Kafka-python-Demo/
├── consumer.py    # Kafka consumer script
├── producer.py    # Kafka producer script
├── pyproject.toml # Poetry dependency file
├── README.md      # Project documentation
└── .gitignore     # Git ignored files
```

---

## 🤝 Contributing
Contributions are welcome! 🚀

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add your feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements
- [Apache Kafka](https://kafka.apache.org/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)

