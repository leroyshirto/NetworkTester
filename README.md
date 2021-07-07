# Network Tester

simple service to test a network between services.

Request is made to the next network tester defined in the env. If no env is set or max depth is reached the request chain is terminated.

Example environment vars of next hop

```env
NEXT_HOP_URL=http://network-tester-hop-4:5000
MAX_DEPTH=10
```

Example response chain

```json
{
  "hop": {
    "hop": {
      "hop": {
        "hop": {
          "hop": {
            "hop": {
              "hop": {
                "last": true,
                "request_end": "Wed, 07 Jul 2021 09:15:54 GMT",
                "request_start": "Wed, 07 Jul 2021 09:15:54 GMT"
              },
              "hostname": "da47be0b90ca",
              "remote_addr": "172.80.38.5"
            },
            "last": false,
            "request_end": "Wed, 07 Jul 2021 09:15:54 GMT",
            "request_start": "Wed, 07 Jul 2021 09:15:54 GMT",
            "status_code": 200
          },
          "hostname": "e504067b08a4",
          "remote_addr": "172.80.38.4"
        },
        "last": false,
        "request_end": "Wed, 07 Jul 2021 09:15:54 GMT",
        "request_start": "Wed, 07 Jul 2021 09:15:54 GMT",
        "status_code": 200
      },
      "hostname": "21508a82e15f",
      "remote_addr": "172.80.38.3"
    },
    "last": false,
    "request_end": "Wed, 07 Jul 2021 09:15:54 GMT",
    "request_start": "Wed, 07 Jul 2021 09:15:54 GMT",
    "status_code": 200
  },
  "hostname": "93d0fb0f0fa6",
  "remote_addr": "172.80.38.1"
}
```
