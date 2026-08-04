class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(node, values):
            if node is None:
                values.append("None")
                return
            values.append(str(node.val))
            preorder(node.left, values)
            preorder(node.right, values)

        values = []
        preorder(root, values)
        return " ".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split()
        i = 0

        def build():
            nonlocal i

            if values[i] == "None":
                i += 1
                return None

            node = TreeNode(int(values[i]))
            i += 1
            node.left = build()
            node.right = build()
            return node

        return build()