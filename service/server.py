import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
class server(Node):
    def __init__(self):
        super().__init__("service_started")
        self.serv=self.create_service(AddTwoInts,'add_two_ints',self.callback)
    def callback(self,request,response):
        response.sum=request.a+request.b
        self.get_logger().info(f"{request.a}+{request.b}")
        return response
    
def main():
    rclpy.init()
    node=server()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()