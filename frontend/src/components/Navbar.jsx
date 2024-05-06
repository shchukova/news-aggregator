import logo from "../assets/logo.jpg";
import { IoIosNotifications } from "react-icons/io";
import { MdOutlineHelp } from "react-icons/md";
import { FaUser } from "react-icons/fa";
import { FaExclamationCircle } from "react-icons/fa";
import { BsArrowRepeat } from "react-icons/bs";
import { TbActivityHeartbeat } from "react-icons/tb";
import { GoAlertFill } from "react-icons/go";

const Navbar = () => {
  return (
    <nav className="bg-white px-4 text-gray-400 rounded-b-xl w-full">
      <div className="bg-white flex justify-between items-center">
        <div className="flex items-center">
          <img className="m-0 w-[60px]" src={logo} alt="logo" />
          <h1 className="text-gray-400 font-bold">Doctors</h1>
        </div>
        <ul className="flex items-center">
          <li className="m-1">
            <IoIosNotifications color="gray" size={20} />
          </li>
          <li className="m-1">
            <MdOutlineHelp color="gray" size={20} />
          </li>
          <li className="m-1">
            <FaUser color="gray" size={20} />
          </li>
        </ul>
      </div>
      <div className="bg-white flex justify-between items-center">
        <div className="flex items-center gap-4">
          <h1>Louise Reed</h1>
          <h1>Corporate</h1>
          <h1>Age 30</h1>
          <FaExclamationCircle color="gray" size={20} />
        </div>
        <div className="text-gray-500 flex items-center gap-3">
          <div className="flex items-center my-1">
            <BsArrowRepeat color="gray" size={20} />
            <h1>Patient Timeline</h1>
          </div>
          <div className="flex items-center my-1">
            <TbActivityHeartbeat color="gray" size={20} />
            <h1>Monitor</h1>
          </div>
          <div className="flex items-center my-1">
            <GoAlertFill color="gray" size={20} />
            <h1>Alert</h1>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
