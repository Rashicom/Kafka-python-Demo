# Kafka-Python-Demo

A simple demo showcasing how to use **Kafka** with **Python** and **KRaft (Kafka Raft Metadata Mode)** to produce and consume real-time temperature data.

## 🚀 Features
- **Producer**: Publishes temperature data to a Kafka topic.
- **Consumer**: Subscribes to a Kafka topic and prints real-time temperature data.
- **Command-line arguments**: Specify topics and user groups dynamically.

---

## 📦 Prerequisites
- **Docker** installed on your machine.
- **Python 3.7+** installed.
- Install Python dependencies:
  ```bash
  pip install kafka-python
  ```

---

## 🐳 Setting Up Kafka with Docker

### 1. Pull the Kafka Docker image:
```bash
docker pull apache/kafka:3.9.0
```

### 2. Run Kafka with KRaft mode:
```bash
docker run -d \
  --name kafka-container \
  -p 9092:9092 \
  apache/kafka:3.9.0
```

This starts Kafka in **KRaft mode** without requiring Zookeeper.

✅ **Kafka Broker Running on:** `localhost:9092`

---

## 📝 Usage

### 1. **Producer**: Send temperature data to a topic.
```bash
python producer.py -t <topic_name>
```

**Example:**
```bash
python producer.py -t temp-topic
```
👉 Enter the location and temperature when prompted. Data is sent to Kafka in real-time.

---

### 2. **Consumer**: Read temperature data from a topic.
```bash
python consumer.py -t <topic_name> -u <user_group>
```

**Example:**
```bash
python consumer.py -t temp-topic -u temp-group
```
👉 The consumer listens for new messages and prints them to the console.

---

## 📂 Project Structure
```
Kafka-python-Demo/
├── producer.py   # Producer script to publish temperature data
├── consumer.py   # Consumer script to consume temperature data
└── README.md     # Project documentation
```

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo, submit issues, or make pull requests.

### Steps to contribute:
1. Fork the repo 📌
2. Create a new branch (`git checkout -b feature-yourFeature`) 🌱
3. Commit your changes (`git commit -m 'Add your feature'`) 💬
4. Push to the branch (`git push origin feature-yourFeature`) 🚀
5. Create a pull request 🔥

---

## 🛡️ License
This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements
- [Apache Kafka](https://kafka.apache.org/)
- [kafka-python](https://github.com/dpkp/kafka-python)
- Docker for seamless containerization 🐳

---

## 🚀 Happy Coding & Streaming Data! 📊📡

