try:
        await client.connect()
    except ConnectionError:
        await client.disconnect()
        await client.connect()