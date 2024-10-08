import { convertCodeForDisplay } from "../../../helpers/utils";
import ComboBox from "../../UI/Form/ComboBox";
import { CAN_TRANSFER } from "../CAN.constants";
/**
 * @typedef {Object} DataProps
 * @property {number} id - The identifier of the data item
 * @property {string | number} title - The title of the data item
 */

/**
 * @component
 * @param {Object} props - The component props.
 * @param {DataProps[]} props.transfer - The current active period.
 * @param {Function} props.setTransfer - A function to call to set the active period.
 * @param {string} [props.legendClassname] - The class name for the legend (optional).
 * @param {string} [props.defaultString] - The default string to display (optional).
 * @param {Object} [props.overrideStyles] - The CSS styles to override the default (optional).
 * @returns {JSX.Element} - The rendered component.
 */
const CANTransferComboBox = ({
    transfer,
    setTransfer,
    legendClassname = "usa-label margin-top-0",
    defaultString = "",
    overrideStyles = { width: "187px" }
}) => {
    const options = [
        { id: 1, title: convertCodeForDisplay("methodOfTransfer", CAN_TRANSFER.DIRECT) },
        { id: 2, title: convertCodeForDisplay("methodOfTransfer", CAN_TRANSFER.COST_SHARE) },
        { id: 3, title: convertCodeForDisplay("methodOfTransfer", CAN_TRANSFER.IDDA) },
        { id: 4, title: convertCodeForDisplay("methodOfTransfer", CAN_TRANSFER.IAA) }
    ];

    return (
        <div className="display-flex flex-justify">
            <div>
                <label
                    className={legendClassname}
                    htmlFor="can-active-period-combobox-input"
                >
                    Transfer
                </label>
                <div>
                    <ComboBox
                        namespace="can-active-period-combobox"
                        data={options}
                        selectedData={transfer}
                        setSelectedData={setTransfer}
                        defaultString={defaultString}
                        overrideStyles={overrideStyles}
                        isMulti={true}
                    />
                </div>
            </div>
        </div>
    );
};

export default CANTransferComboBox;
