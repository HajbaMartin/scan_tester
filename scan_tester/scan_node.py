import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

class ScanNode(Node):
    def __init__(self):
        super().__init__('scan_node')
        self.get_logger().info("A node elindult: scan_node")

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.publisher = self.create_publisher(String, '/status_info', 10)

    def scan_callback(self, msg: LaserScan):
        min_distance = min(msg.ranges)
        out_msg = String()
        out_msg.data = f"Legkisebb mért távolság: {min_distance:.2f} méter"
        self.publisher.publish(out_msg)
        self.get_logger().info(out_msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = ScanNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
