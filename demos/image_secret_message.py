if __name__ == '__main__':
        
    # pip install stegano
    from stegano import lsb
    # hide secret message in image
    secret = lsb.hide(r'static\images\Hydrangeas.jpg', 'Secret Message: This is the test of message file name Hydrangeas.jpg')
    
    # save image with hidden message
    secret.save(r'static\images\secret_img.png')
    

    # reveal hidden secret message in image
    print(lsb.reveal(r'static\images\secret_img.png'))

    #Output -> Your secret message

    