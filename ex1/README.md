# kafka_examples
This repo has some sort of kafka python code examples

* install Kafka-Python. You can do this using pip or conda, if you’re using an Anaconda distribution.
```bash
pip install kafka-python
```
```bash
conda install -c conda-forge kafka-python
```
* Don’t forget to start your **Zookeeper** server and **Kafka broker** before executing the example code below. In this example we assume that **Zookeeper** is running default on **localhost:2181** and Kafka on **localhost:9092**.

* Using a topic called numtest in this example, you can create a new topic by opening a new command prompt
```bash
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic numtest
```

* In our example, we’ll create a producer that emits numbers from 1 to 1000 and send them to our Kafka broker. Then a consumer will read the data from the broker and store them

