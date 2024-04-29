import React, { useState } from "react";
import Header from "../components/Header";

function LB4Page() {
  const [pair1, setPair1] = useState("");

  const handleChangePair1 = (event) => {
    let value = event.target.value;
    if (value.length > 3) {
      value = value.slice(0, 5);
    }
    setPair1(value);
  };
  return (
    <div>
      <Header />
      <div className="input">
        <div className="left_block">
          <div className="input_coordinates">
            <label>
              <input
                type="text"
                placeholder="First coordinates"
                value={pair1}
                onChange={handleChangePair1}
                style={{ color: "white" }}
              />
            </label>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LB4Page;
