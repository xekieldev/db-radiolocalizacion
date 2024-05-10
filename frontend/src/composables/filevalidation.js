export function useFileValidation() {

    const fileRegEx1 = /^EX-\d{4}-\d{6,10}-\s{1,3}-[A-Z]{3,7}-[A-Z]{3,10}#[A-Z]{2,8}$/
    const fileRegEx2 = /^IF-\d{4}-\d{8}-[A-Z]{3}-[A-Z]{2,5}#[A-Z]{6}$/
    const fileRegEx3 = /^NO-\d{4}-\d{8}-[A-Z]{3,8}-[A-Z]{2,10}#?[A-Z]{6}?$/
    const fileRegEx4 = /^[A-Z]{5,20}\s?E?\s?\s\d{1,8}\/\d{4}$/
    const fileRegEx5 = /^A\s{1}definir$/

    const getComposedRegex = (...regexes) => new RegExp(regexes.map(regex => regex.source).join("|"))


    const fileRegEx = getComposedRegex(fileRegEx1, fileRegEx2, fileRegEx3, fileRegEx4, fileRegEx5)
    const validateFile = file => !!file.value.match(fileRegEx)

    return { validateFile }
}