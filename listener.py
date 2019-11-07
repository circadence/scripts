from azure.storage.common import CloudStorageAccount
import config

def main():
    print("Hello World!")
    try:
        account = CloudStorageAccount(config.STORAGE_ACCOUNT_NAME,config.STORAGE_ACCOUNT_KEY)
        queue_service = account.create_queue_service()
        queue_service.create_queue(config.STORAGE_QUEUE_NAME)
        while True:
            try:
                messages = queue_service.get_messages(config.STORAGE_QUEUE_NAME)
                for message in messages:
                    print('Message for dequeueing is: ', message.content)
                    # Then delete it.
                    # When queue is deleted all messages are deleted, here is done for demo purposes 
                    # Deleting requires the message id and pop receipt (returned by get_messages)
                    queue_service.delete_message(config.STORAGE_QUEUE_NAME, message.id, message.pop_receipt)
                    print('Successfully dequeued message')
            except Exception as e:
                print('Error occurred get_messages:', e)
                continue
    except Exception as e:
        print('Error occurred:', e)

if __name__ == "__main__":
    main()
