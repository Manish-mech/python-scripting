# python-scripting

A collection of Python scripts for automating and simplifying common DevOps and cloud infrastructure tasks.

---

## 📄 `cidr_block.py`

This script breaks down a VPC CIDR block into a specified number of equal-sized subnet CIDRs using Python’s built-in `ipaddress` module.

### 🔧 What it does:
- Prompts the user for a VPC CIDR block (e.g., `10.0.0.0/16`)
- Asks for the number of subnets required
- Calculates and displays the subnet CIDRs accordingly

### 🧰 Use Case:
Perfect for planning subnets while designing AWS VPCs or any cloud-based network infrastructure (terraform).
