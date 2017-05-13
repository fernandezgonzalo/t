# t
micro task manager, ispired by [http://stevelosh.com/projects/t/](http://stevelosh.com/projects/t/)

## Install

1. Clone the repo
2. pip3 install -r requirements.txt
3. echo "alias t='python3 absolute_route_main.py'" >> ~/.bash_profile
4. run

## Usage

### Add new Task
```
$ t a Buy potatoes

```

or if you want to specify a priority, for default priority is 0
```
$ t a Buy potatoes -p NUM
```

### List tasks, ordered by priority
```
$ t
```

or

```
$ t l
```


### Edit task
```
$ t e ID text
```

### Remove task
```
$ t r ID
```