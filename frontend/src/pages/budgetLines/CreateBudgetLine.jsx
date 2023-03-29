import App from "../../App";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { StepIndicatorOne } from "../../components/UI/StepIndicator/StepIndicatorOne";
import { StepIndicatorTwo } from "../../components/UI/StepIndicator/StepIndicatorTwo";
import { StepIndicatorThree } from "../../components/UI/StepIndicator/StepIndicatorThree";
import { CreateBudgetLineFlow } from "./CreateBudgetLineFlow";
import { ProjectSelect } from "./ProjectSelect";
import { AgreementSelect } from "./AgreementSelect";
import { CanSelect } from "./CanSelect";
import { DesiredAwardDate } from "./DesiredAwardDate";
import { getAgreementsByResearchProjectFilter } from "../../api/getAgreements";
import {
    setAgreements,
    setBudgetLineAdded,
    setEnteredDescription,
    setEnteredAmount,
    setSelectedCan,
    setEnteredMonth,
    setEnteredYear,
    setEnteredDay,
    setEnteredComments,
} from "./createBudgetLineSlice";
import { ProcurementShopSelect } from "./ProcurementShopSelect";

const StepOne = ({ goToNext }) => (
    <>
        <h2 className="font-sans-lg">Create New Budget Line</h2>
        <p>Step One: Text explaining this page</p>
        <StepIndicatorOne />
        <h2 className="font-sans-lg">Select a Project</h2>
        <p>
            Select the project this budget line should be associated with. If you need to create a new project, click
            Add New Project.
        </p>
        <ProjectSelect />
        <h2 className="font-sans-lg">Select an Agreement</h2>
        <p>Select the project and agreement this budget line should be associated with.</p>
        <AgreementSelect />
        <div className="grid-row flex-justify-end margin-top-8">
            <button className="usa-button" onClick={() => goToNext({ project: "Red X 2.0" })}>
                Continue
            </button>
        </div>
        <div className="display-flex flex-align-center margin-top-6">
            <div className="border-bottom-1px border-base-light width-full" />
            <span className="text-base-light margin-left-2 margin-right-2">or</span>
            <div className="border-bottom-1px border-base-light width-full" />
        </div>
        <div className="grid-row flex-justify-center">
            <button className="usa-button usa-button--outline margin-top-6 margin-bottom-6">Add New Project</button>
            <button className="usa-button usa-button--outline margin-top-6 margin-bottom-6">Add New Agreement</button>
        </div>
    </>
);
const StepTwo = ({ goBack, goToNext }) => {
    const dispatch = useDispatch();
    const budgetLinesAdded = useSelector((state) => state.createBudgetLine.budget_lines_added);
    const selectedCan = useSelector((state) => state.createBudgetLine.selected_can);
    const enteredDescription = useSelector((state) => state.createBudgetLine.entered_description);
    const enteredAmount = useSelector((state) => state.createBudgetLine.entered_amount);
    const enteredMonth = useSelector((state) => state.createBudgetLine.entered_month);
    const enteredDay = useSelector((state) => state.createBudgetLine.entered_day);
    const enteredYear = useSelector((state) => state.createBudgetLine.entered_year);
    const enteredComments = useSelector((state) => state.createBudgetLine.entered_comments);
    const selectedProcurementShop = useSelector((state) => state.createBudgetLine.selected_procurement_shop);
    const selectedResearchProject = useSelector((state) => state.createBudgetLine.selected_project);
    const selectedAgreement = useSelector((state) => state.createBudgetLine.selected_agreement);

    const handleSubmitForm = (e) => {
        e.preventDefault();
        dispatch(
            setBudgetLineAdded([
                ...budgetLinesAdded,
                {
                    id: crypto.getRandomValues(new Uint32Array(1))[0],
                    line_description: enteredDescription,
                    comments: enteredComments,
                    can_id: selectedCan?.id,
                    can_number: selectedCan?.number,
                    agreement_id: selectedAgreement?.id,
                    amount: enteredAmount,
                    status: "DRAFT",
                    date_needed: `${enteredYear}-${enteredMonth}-${enteredDay}`,
                    psc_fee_amount: selectedProcurementShop?.fee,
                },
            ])
        );
        //reset form
        dispatch(setEnteredDescription(""));
        dispatch(setEnteredAmount(null));
        dispatch(setSelectedCan({}));
        dispatch(setEnteredMonth(""));
        dispatch(setEnteredDay(""));
        dispatch(setEnteredYear(""));
        dispatch(setEnteredComments(""));
        alert("Budget Line Added");
    };
    return (
        <>
            <h2 className="font-sans-lg">Create New Budget Line</h2>
            <p>Step Two: Text explaining this page</p>
            <StepIndicatorTwo />
            <h2 className="font-sans-lg">Procurement Shop</h2>
            <p>
                Select the Procurement Shop, and the fee rates will be populated in the table below. If this is an
                active agreement, it will default to the procurement shop currently being used.
            </p>
            <ProcurementShopSelect />
            <h2 className="font-sans-lg margin-top-3">Budget Line Details</h2>
            <p>
                Complete the information below to create new budget lines. Select Add Budget Line to create multiple
                budget lines.
            </p>
            <form className="grid-row grid-gap">
                <div className="grid-col-4">
                    <div className="usa-form-group">
                        <label className="usa-label" htmlFor="bl-description">
                            Description
                        </label>
                        <input
                            className="usa-input"
                            id="bl-description"
                            name="bl-description"
                            type="text"
                            value={enteredDescription || ""}
                            onChange={(e) => dispatch(setEnteredDescription(e.target.value))}
                        />
                    </div>
                    <div className="usa-form-group">
                        <CanSelect />
                    </div>
                </div>
                <div className="grid-col-4">
                    <DesiredAwardDate />
                    <div className="usa-form-group">
                        <label className="usa-label" htmlFor="bl-amount">
                            Amount
                        </label>
                        <input
                            className="usa-input"
                            id="bl-amount"
                            name="bl-amount"
                            type="number"
                            value={enteredAmount || ""}
                            placeholder="$"
                            onChange={(e) => dispatch(setEnteredAmount(Number(e.target.value)))}
                        />
                    </div>
                </div>
                <div className="grid-col-4">
                    <div className="usa-character-count">
                        <div className="usa-form-group">
                            <label className="usa-label" htmlFor="with-hint-textarea">
                                Notes (optional)
                            </label>
                            <span id="with-hint-textarea-hint" className="usa-hint">
                                Maximum 150 characters
                            </span>
                            <textarea
                                className="usa-textarea usa-character-count__field"
                                id="with-hint-textarea"
                                maxLength="150"
                                name="with-hint-textarea"
                                rows="5"
                                aria-describedby="with-hint-textarea-info with-hint-textarea-hint"
                                style={{ height: "7rem" }}
                                value={enteredComments || ""}
                                onChange={(e) => dispatch(setEnteredComments(e.target.value))}
                            ></textarea>
                        </div>
                        <span id="with-hint-textarea-info" className="usa-character-count__message sr-only">
                            You can enter up to 150 characters
                        </span>
                    </div>
                    <button
                        className="usa-button usa-button--outline margin-top-2 float-right margin-right-0"
                        onClick={handleSubmitForm}
                    >
                        Add Budget Line
                    </button>
                </div>
            </form>
            {/* NOTE: BLI Preview Table */}
            <h2 className="font-sans-lg">Budget Lines</h2>
            <p>
                This is a list of all budget lines for the selected project and agreement. The budget lines you add will
                display in draft status. The Fiscal Year (FY) will populate based on the election date you provide.
            </p>
            <div className="font-family-sans font-12px">
                <dl className="margin-0 padding-y-2 padding-x-105">
                    <dt className="margin-0 text-base-dark">Project</dt>
                    <dd className="text-semibold margin-0">{selectedResearchProject?.title}</dd>
                    <dt className="margin-0 text-base-dark margin-top-2">Agreement</dt>
                    <dd className="text-semibold margin-0">{selectedAgreement?.name}</dd>
                </dl>
            </div>
            <table className="usa-table usa-table--borderless">
                <thead>
                    <tr>
                        <th scope="col">Description</th>
                        <th scope="col">Need By</th>
                        <th scope="col">FY</th>
                        <th scope="col">CAN</th>
                        <th scope="col">Amount</th>
                        <th scope="col">Fee</th>
                        <th scope="col">Total</th>
                        <th scope="col">Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">SC1</th>
                        <td>9/30/2021</td>
                        <td>2023</td>
                        <td>G99CC23</td>
                        <td>$500,000.00</td>
                        <td>$10,000.00</td>
                        <td>$510,000.00</td>
                        <td>Draft</td>
                    </tr>
                    {budgetLinesAdded.map((bl) => {
                        // Format the date like this 9/30/2023 || MM/DD/YYYY
                        let date_needed = new Date(bl.date_needed);
                        const formatted_date_needed = `${
                            date_needed.getMonth() + 1
                        }/${date_needed.getDate()}/${date_needed.getFullYear()}`;
                        let month = date_needed.getMonth();
                        let year = date_needed.getFullYear();
                        // FY will automate based on the Need by Date. Anything after September 30th rolls over into the next FY.
                        let fiscalYear = month > 8 ? year + 1 : year;
                        let feeTotal = bl.amount * (bl.psc_fee_amount / 10);
                        let total = bl.amount + feeTotal;
                        let status = bl.status.charAt(0).toUpperCase() + bl.status.slice(1).toLowerCase();
                        // Format the amounts like this $500,000.00 || $1,000,000.00 to allow for commas
                        let formattedAmount = `$${bl.amount.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, "$&,")}`;
                        let formattedFeeTotal = `$${feeTotal.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, "$&,")}`;
                        let formattedTotal = `$${total.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, "$&,")}`;
                        return (
                            <tr key={bl.id}>
                                <th scope="row">{bl.line_description}</th>
                                <td>{formatted_date_needed}</td>
                                <td>{fiscalYear}</td>
                                <td>{bl.can_number}</td>
                                <td>{formattedAmount}</td>
                                <td>{feeTotal === 0 ? 0 : formattedFeeTotal}</td>
                                <td>{total === 0 ? 0 : formattedTotal}</td>
                                <td>{status}</td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
            <div className="grid-row flex-justify-end margin-top-1">
                <button className="usa-button usa-button--outline" onClick={() => goBack()}>
                    Back
                </button>
                <button className="usa-button" onClick={() => goToNext({ name: "John Doe" })}>
                    Continue
                </button>
            </div>
        </>
    );
};

const StepThree = ({ goBack, goToNext }) => (
    <>
        <h2 className="font-sans-lg">Create New Budget Line</h2>
        <p>Step Three: Text explaining this page</p>
        <StepIndicatorThree />

        <div className="grid-row flex-justify-end">
            <button className="usa-button usa-button--outline" onClick={() => goBack()}>
                Back
            </button>
            <button className="usa-button" onClick={() => goToNext({ name: "John Doe" })}>
                Continue
            </button>
        </div>
    </>
);

export const CreateBudgetLine = () => {
    const dispatch = useDispatch();
    const selectedProject = useSelector((state) => state.createBudgetLine.selectedProject);

    // Get initial list of Agreements (dependent on Research Project Selection)
    useEffect(() => {
        const getAgreementsAndSetState = async () => {
            if (selectedProject) {
                const agreements = await getAgreementsByResearchProjectFilter(selectedProject?.id);
                dispatch(setAgreements(agreements));
            }
        };

        getAgreementsAndSetState().catch(console.error);

        return () => {
            dispatch(setAgreements([]));
        };
    }, [dispatch, selectedProject]);

    return (
        <App>
            <CreateBudgetLineFlow
                onFinish={(data) => {
                    console.log("budget line has: " + JSON.stringify(data, null, 2));
                    alert("Budget Line Created!");
                }}
            >
                <StepOne />
                <StepTwo />
                <StepThree />
            </CreateBudgetLineFlow>
        </App>
    );
};
