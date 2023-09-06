import { Provider } from "react-redux";
import { render, screen } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import AgreementsTable from "./AgreementsTable";
import configureStore from "redux-mock-store";

const mockStore = configureStore([]);
const agreements = [
    {
        id: 1,
        name: "Test Agreement",
        research_project: { title: "Test Project" },
        agreement_type: "GRANT",
        project_officer: 1,
        team_members: [{ id: 1 }],
        procurement_shop: { fee: 0.05 },
        budget_line_items: [
            { amount: 100, date_needed: "2024-05-02T11:00:00", status: "DRAFT" },
            { amount: 200, date_needed: "2023-03-02T11:00:00", status: "UNDER_REVIEW" },
        ],
        created_by: 1,
        notes: "Test notes",
        created_on: "2021-10-21T03:24:00",
        status: "In Review",
    },
];
const userData = {
    id: 1,
    full_name: "Test User",
};

jest.mock("../../../api/opsAPI", () => ({
    ...jest.requireActual("../../../api/opsAPI"),
    useGetUserByIdQuery: () => jest.fn(() => ({ data: userData })),
}));

const initialState = {
    auth: {
        activeUser: {
            id: 1,
            name: "Test User",
        },
    },
};
const store = mockStore(initialState);

it("renders without crashing", () => {
    render(
        <Provider store={store}>
            <BrowserRouter>
                <AgreementsTable agreements={agreements} />
            </BrowserRouter>
        </Provider>
    );
    expect(screen.getByText("Test Agreement")).toBeInTheDocument();
    expect(screen.getByText("Test Project")).toBeInTheDocument();
    expect(screen.getByText("Grant")).toBeInTheDocument();
    expect(screen.getByText("$315.00")).toBeInTheDocument();
    expect(screen.getByText("3/2/2023")).toBeInTheDocument();
});
