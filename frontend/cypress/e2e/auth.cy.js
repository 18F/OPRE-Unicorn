/// <reference types="cypress" />
import { logout } from "../../src/components/Auth/authSlice";
import { terminalLog, testLogin } from "./utils";

beforeEach(() => {
    cy.visit("/");
});

it("sign in button visible at page load when there is no jwt", () => {
    cy.session("anonymous", () => {
        cy.visit("/");
        cy.contains("Sign-in");
    });
});

it("access_token is present within localstorage after login", () => {
    testLogin("admin");
    cy.getLocalStorage("access_token").should("exist");
});

it.skip("********* DEBUGGING clicking logout removes the jwt and displays sign-in", () => {
    cy.visit("/");
    testLogin("admin");
    cy.contains("Sign-out").click();
    cy.window().its("localStorage").invoke("getItem", "access_token").should("not.exist");
    cy.window()
        .then((win) => win.store.getState().auth)
        .should("deep.include", { isLoggedIn: false });
    cy.contains("Sign-in");
    cy.url("/");
});

it("isLoggedIn state is false when there is no jwt", () => {
    cy.visit("/");
    cy.window()
        .then((win) => win.store.getState().auth)
        .should("deep.include", { isLoggedIn: false });
});

it("isLoggedIn state is true when there is a jwt", () => {
    cy.visit("/");
    testLogin("admin");
    cy.window()
        .then((win) => win.store.getState().auth)
        .should("deep.include", { isLoggedIn: true });
});

it("Sign Out button visible when user is Authenticated", () => {
    cy.visit("/");
    testLogin("admin");
    cy.contains("Sign-out");
});
