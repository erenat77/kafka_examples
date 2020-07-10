# kafka_example-2

* install Kafka-Python. You can do this using pip or conda, if you’re using an Anaconda distribution.
```bash
pip install kafka-python
```
```bash
conda install -c conda-forge kafka-python
```
* Don’t forget to start your **Zookeeper** server and **Kafka broker** before executing the example code below. In this example we assume that **Zookeeper** is running default on **localhost:2181** and Kafka on **localhost:9092**.


* In our example, instead of showing you a simple example to run Kafka Producer and Consumer separately, I’ll show the JSON serializer and deserializer.

