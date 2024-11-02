import train
import test
import data_loader
import check_environment

def main():
    # Check environment first
    check_environment.main()
    
    print("Starting data processing...")
    data_loader.main()
    print("Training model...")
    train.main()
    test.main()

if __name__ == '__main__':
    main()
