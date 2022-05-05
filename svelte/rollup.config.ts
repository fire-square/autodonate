import svelte from 'rollup-plugin-svelte';
import commonjs from '@rollup/plugin-commonjs';
import resolve from '@rollup/plugin-node-resolve';
import livereload from 'rollup-plugin-livereload';
import { terser } from 'rollup-plugin-terser';
import sveltePreprocess from 'svelte-preprocess';
import typescript from '@rollup/plugin-typescript';
import css from 'rollup-plugin-css-only';
import * as child_process from 'child_process';
import type { CssHashGetter } from 'svelte/types/compiler/interfaces';

const production = !process.env.ROLLUP_WATCH;

const get_css_hash: CssHashGetter = ({ css, hash }) => {
	return `donate-${hash(css)}`;
};

function serve() {
    let server: child_process.ChildProcess;

    function toExit() {
        if (server) server.kill(0);
    }

    return {
        writeBundle() {
            if (server) return;
            server = child_process.spawn('npm', ['run', 'start', '--', '--dev'], {
                stdio: ['ignore', 'inherit', 'inherit'],
                shell: true
            });

            process.on('SIGTERM', toExit);
            process.on('exit', toExit);
        }
    };
}

function componentExportDetails(componentName: string) {
    return {
        input: `src/declarations/${componentName.toLowerCase()}.ts`,
        output: {
            sourcemap: !production,
            format: 'iife',
            name: `${componentName.toLowerCase()}`,
            file: `public/build/svelte/${componentName.toLowerCase()}.js`,
        },
        plugins: [
            svelte({
                compilerOptions: {
                    // enable run-time checks when not in production
                    dev: !production,
                    cssHash: get_css_hash
                },
                // TypeScript preprocessing
                preprocess: sveltePreprocess({ sourceMap: !production })
            }),
            // we'll extract any component CSS out into
            // a separate file - better for performance
            css({ output: `bundle.css` }),

            // If you have external dependencies installed from
            // npm, you'll most likely need these plugins. In
            // some cases you'll need additional configuration -
            // consult the documentation for details:
            // https://github.com/rollup/plugins/tree/master/packages/commonjs
            resolve({
                browser: true,
                dedupe: ['svelte']
            }),
            commonjs(),

            // Some TypeScript options.
            typescript({
                sourceMap: !production,
                inlineSources: !production
            }),

            // In dev mode, call `npm run start` once
            // the bundle has been generated
            !production && serve(),

            // Watch the `public` directory and refresh the
            // browser on changes when not in production
            !production && livereload('public'),

            // If we're building for production (npm run build
            // instead of npm run dev), minify
            production && terser()
        ],
        watch: {
            clearScreen: false
        }
    };
}

let exportable = [];

[
    "Admin",
    "AdminPages",
].forEach((d) => exportable.push(componentExportDetails(d)));

export default exportable;
