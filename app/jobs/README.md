# Celery

A job queue based on distributed messaging

# How To Start

Create a job function like bellow first

```python
@celery.task
def update_user_source(ifa, phone):
    records = db.session().query(Advertisement).filter_by(ifa=ifa).all()
    if len(records) == 0:
        return
    selected = sorted(records, key=lambda x: x.create_time, reverse=True)[0]
    source = Advertisement.AD_SOURCE_MAP[selected.ad_service]
    user = db.session().query(Customer).filter_by(phone=phone).first()
    user.source = source
    db.session.add(user)
    db.session.commit()

```

Then add Celery Decorator ``celery.task``

create a process to let queue work

```shell
$ celery -A tasks worker
```

# Use It In Your Business

just like using a func
```python
 update_user_source.delay(idfa,phone)
```

