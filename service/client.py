import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
# class client(Node):
#    def __init__(self):
#        super().__init__("node")
#        self.cli=self.create_client(
#            AddTwoInts,
#            'add_two_ints'
#        )
#        while not self.cli.wait_for_service(1.0):
#            self.get_logger().info("waiting for service")
#        self.re=AddTwoInts.Request()
#    def res(self,i,j):
#        self.re.a=i
#        self.re.b=j
#        return self.cli.call_async(self.re)


# def main(args=None):
#     rclpy.init(args=args)
#     node=client()
#     future=node.res(10,20)
#     rclpy.spin_until_future_complete(node, future)

#     if future is not None:
#         ah=future.result()
#         node.get_logger().info(str(ah.sum))
#     rclpy.shutdown()
# if __name__=="__main__":
#     main()                                                                                                                                                            
class service(Node):
    def __init__(self):
        super().__init__("koshish")
        self.cli=self.create_client(AddTwoInts,'add_two_ints')
        while not self.cli.wait_for_service(1.0):
            self.get_logger().info("waiting for  service")
        self.re=AddTwoInts.Request()
    def res(self,i,j):
        self.re.a=i 
        self.re.b=j 
        future=self.cli.call_async(self.re)
        future.add_done_callback(self.callback)
    def callback(self,future):
        result=future.result()
        self.get_logger().info(str(result.sum))


        
def main(args=None):
        rclpy.init(args=args)
        node=service()
        node.res(3,5)
        rclpy.spin(node)
        rclpy.shutdown()

if __name__=="__main__":
    main()
