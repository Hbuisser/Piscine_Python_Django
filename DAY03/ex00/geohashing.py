import sys
import antigravity

def geohashing():
    if len(sys.argv) == 4:
        try:
            antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode())
        except Exception as error:
            print(error)
    else:
        print("Wrong number of parameters")

if __name__ == "__main__":
    geohashing()
    
	# antigravity.geohash(100,120,b'2020-12-06 30218.26')
	# 37.421542, -122.085589, b'2005-05-26-10458.68'
	# https://github.com/OrkoHunter/python-easter-eggs/issues/2
