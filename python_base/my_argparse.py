import argparse

# parser = argparse.ArgumentParser(description='process some integers.')
# parser.add_argument('integers' , metavar='N' , type=int , nargs='+' , help="an integer for the accumulator")
# parser.add_argument('--sum' , dest='accumulate' , action='store_const' , const=sum , default=max , help="sum the integers (default : find the max)")
# args = parser.parse_args()
# print(args.accumulate(args.integers))

# import argparse
#
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))

parser = argparse.ArgumentParser(description="get squery")
# parser.add_argument('sqy')
# parser.add_argument('-v' , '--var')
#parser.add_argument('-v','--var', action='store_true' , help='this v is my')
#args = parser.parse_args()
#if args.var:
#    print "args is %s" % args.var

#type
#parser.add_argument('x' , type=int , help='x is integer')
#args = parser.parse_args()
#y = args.x ** 2
#print(y)

#choices
parser.add_argument('num' , type=int , help="a num need input")
parser.add_argument('-type' , type=int , choices=[1,2,3] ,help='display type')
args , unparse = parser.parse_known_args()
quer = args.num ** 2
if args.type == 3:
    print('%d squery is %d' % (args.num , quer))
elif args.type == 2:
    print("{}^2={}".format(args.num , quer))
else:
    print(quer)

#print(args)
#print(unparse)

