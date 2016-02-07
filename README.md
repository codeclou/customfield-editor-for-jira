# REST API CLI Client 

![](https://codeclou.github.io/customfield-editor-plugin/data/cep-logo-32.png)

## Customfield Editor Plugin for Atlassian JIRA®

This is a reference implementation of a cli-client written in python for the [Customfield Editor Plugin](http://codeclou.io/redirect/r.php?r=lkmwyvgm) for Atlassian JIRA®.

:exclamation: **The REST CLI Client does not intend to implement all available API features. It only demonstrates basic usage examples.**
 
See the full documentation and usage on the [REST CLI Client page](http://codeclou.io/redirect/r.php?r=alxpzlvx).

The client is compatible to [API version 1.2](https://codeclou.github.io/customfield-editor-plugin/1.2/) of Customfield Editor Plugin.

### Prerequisites

You will need python 3.2+ to build and use the client.

### Usage

cd into dir where `setup.py` resides

```
$> python setup.py install
```

Now you can run the client with:

```
$> cep-client -h
```

Example: List fields as admin user

```
cep-client -a adminListFields -url http://localhost:2990/jira -user admin -pass admin
```

### Screenshot

![](https://codeclou.github.io/customfield-editor-plugin/doc/cep-client-screen-01.png)
