# protobufp

## setup
```
❯ python -V
Python 3.7.2

❯ brew install protobuf
...

❯ protoc --version
libprotoc 3.7.1
```

```
❯ pip install protobuf
```

## compile

```
❯ protoc --python_out=. addressbook.proto
```

## write message

```
❯ python writer.py

```


## read message

```
❯ python reader.py -f addressbook.bin
Person ID : 100
Person Name : John
Person email : email@example.com
Phone Number : 111-2222-3333 [Work]
```

## Developer Guide

https://developers.google.com/protocol-buffers/docs/pythontutorial
