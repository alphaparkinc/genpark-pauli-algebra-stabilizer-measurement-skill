import sys
import json
from client import PauliAlgebra

matrices = {
    "I": PauliAlgebra.I,
    "X": PauliAlgebra.X,
    "Y": PauliAlgebra.Y,
    "Z": PauliAlgebra.Z
}

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "pauli_commutator",
                        "description": "Compute matrix commutator [A, B] = AB - BA between Pauli operators",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "op1": {"type": "string", "enum": ["I", "X", "Y", "Z"]},
                                "op2": {"type": "string", "enum": ["I", "X", "Y", "Z"]}
                            },
                            "required": ["op1", "op2"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "pauli_commutator":
            m1 = matrices[args["op1"]]
            m2 = matrices[args["op2"]]
            comm = PauliAlgebra.commutator(m1, m2)
            out = [[[c.real, c.imag] for c in row] for row in comm]
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"commutator": out})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
