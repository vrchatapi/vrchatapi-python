"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.flattenRoutePaths = void 0;
const shared_utils_1 = require("@nestjs/common/utils/shared.utils");
function flattenRoutePaths(routes) {
    const result = [];
    routes.forEach(item => {
        if (item.module && item.path) {
            result.push({ module: item.module, path: item.path });
        }
        if (item.children) {
            const childrenRef = item.children;
            childrenRef.forEach(child => {
                if (typeof child !== 'string' && child.path) {
                    child.path = shared_utils_1.normalizePath(shared_utils_1.normalizePath(item.path) + shared_utils_1.normalizePath(child.path));
                }
                else {
                    result.push({ path: item.path, module: child });
                }
            });
            result.push(...flattenRoutePaths(childrenRef));
        }
    });
    return result;
}
exports.flattenRoutePaths = flattenRoutePaths;
